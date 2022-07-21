from typing import List, Dict, Any, Optional
import numpy as np
import torch
import cv2

import vista
from buffered_dataset import BufferedDataset
from utils import transform_rgb, RejectionSampler

__all__ = ['VistaDataset', 'worker_init_fn']


class VistaDataset(BufferedDataset):
    def __init__(self,
                 trace_paths: List[str],
                 trace_config: Dict[str, Any],
                 car_config: Dict[str, Any],
                 camera_config: Dict[str, Any],
                 train: Optional[bool] = False,
                 buffer_size: Optional[int] = 1,
                 snippet_size: Optional[int] = 100,
                 shuffle: Optional[bool] = False,
                 **kwargs):
        super(VistaDataset,
              self).__init__(trace_paths, trace_config, car_config, train,
                             buffer_size, snippet_size, shuffle)

    def _simulate(self):
        # Initialization for singl-processing dataloader
#        worker_info = torch.utils.data.get_worker_info()
#        if worker_info is None:
        self._world = vista.World(self.trace_paths, self.trace_config)
        self._agent = self._world.spawn_agent(self.car_config)
        self._camera = self._agent.spawn_camera(self.camera_config)
        self._world.reset()
        self._sampler = RejectionSampler()

        # Data generator from simulation
        self._snippet_i = 0
        while True:
            # reset simulator
            if self._agent.done or self._snippet_i >= self.snippet_size:
                self._world.reset()
                self._snippet_i = 0

            # step simulator
            sensor_name = self._camera.name
            img = self._agent.observations[
                sensor_name]  # associate action t with observation t-1
            self._agent.step_dataset(step_dynamics=False)

            # rejection sampling
            val = self._agent.human_curvature
            sampling_prob = self._sampler.get_sampling_probability(val)
            if self._rng.uniform(0., 1.) > sampling_prob:
                self._snippet_i += 1
                continue
            self._sampler.add_to_history(val)

            # preprocess and produce data-label pairs
            img = transform_rgb(img, self._camera, self.train)
            label = np.array([self._agent.human_curvature]).astype(np.float32)
            print(label)

            self._snippet_i += 1
            
            display = vista.Display(self._world, 30)
            
            vis_img = display.render()
            cv2.imshow('Visualize control', vis_img[:, :, ::-1])
            cv2.waitKey(20)

            yield {'camera': img, 'target': label}
            
    @property
    def camera_config(self) -> Dict[str, Any]:
        return self._camera_config


def worker_init_fn(worker_id):
    worker_info = torch.utils.data.get_worker_info()
    dataset = worker_info.dataset
    dataset._world = vista.World(dataset.trace_paths, dataset.trace_config)
    dataset._agent = dataset._world.spawn_agent(dataset.car_config)
    dataset._camera = dataset._agent.spawn_camera(dataset.camera_config)
    dataset._world.set_seed(worker_id)
    dataset._world.reset()
    dataset._sampler = RejectionSampler()


def main():
    v = VistaDataset(trace_paths = '/Users/grace/Documents/vista_traces/20210726-131322_lexus_devens_center',
        trace_config = dict(road_width=4,
                        reset_mode='default',
                        master_sensor='camera_front',
                        ),
        car_config = dict(
            length=5.,
            width=2.,
            wheel_base=2.78,
            steering_ratio=14.7,
            lookahead_road=True,
        ),
          camera_config = {'name': 'camera_front',
         'rig_path': './RIG.xml',
         'size': (200, 320)},
          train = True, buffer_size = 1, snippet_size = 100, shuffle = True)

    v._simulate()
