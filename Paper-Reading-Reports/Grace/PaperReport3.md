## Facilitating Vulnerability Assessment through PoC Migration
[Link to original article](https://github.com/wangfra27/HIL-Computer-Simulation-of-Intelligent-Cybersecurity/blob/main/Summer%20Research%202022/Conference%20Papers/ACM_CCS_2021/Facilitating%20Vulnerability%20Assessment%20through%20PoC%20Migration.pdf)
### Probem: 
More than 150k software vulnerablities are indexed and made vulnerability reports that include its vulnerable software versions, the severity, and a Proof-of-Concept (PoC) that can reproduce the failure regarding the vulnerability. This archive is important because it helps developers manage and avoid these vulnerabilities for better security in the future. However, multiple recent research works have shown that vulnerablity reports often have incorrect or missing information regarding the vulnerable software, therefore imposing greater security risks.

### Proposed Solution:
Migrate a PoC across different versions of the same software in order to perform a vulnerability assessment. This will be a systematic, automated approach, which they named VulScope.

### Methodology

### Results
After conducting experiments on 30 CVEs (commmon vulnerabilities and exposures) on 470 versions of software, it was found the VulScope results in no false positives and only 7.9% false negatives. When compared to other methods solving the same issue, VulScope signficantly outperforms. 
