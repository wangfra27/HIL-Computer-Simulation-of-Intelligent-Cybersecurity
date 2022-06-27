## Facilitating Vulnerability Assessment through PoC Migration
[Link to original article](https://github.com/wangfra27/HIL-Computer-Simulation-of-Intelligent-Cybersecurity/blob/main/Summer%20Research%202022/Conference%20Papers/ACM_CCS_2021/Facilitating%20Vulnerability%20Assessment%20through%20PoC%20Migration.pdf)
### Probem: 
More than 150k software vulnerablities are indexed and made vulnerability reports that include its vulnerable software versions, the severity, and a Proof-of-Concept (PoC) that can reproduce the failure regarding the vulnerability. This archive is important because it helps developers manage and avoid these vulnerabilities for better security in the future. However, multiple recent research works have shown that vulnerablity reports often have incorrect or missing information regarding the vulnerable software, therefore imposing greater security risks.

### Proposed Solution:
Migrate a PoC across different versions of the same software in order to perform a vulnerability assessment. This will be a systematic, automated approach, which they named VulScope. This PoC migration process will first locate the differences between reference code and the target code on a function-level, and the adjusts the PoC to make a new target code that is more similar to the reference code. This is important in order to minimize syntatic and semantic differences in code so that the PoC can trigger the same vulnerabilities. 

<img width="466" alt="image" src="https://user-images.githubusercontent.com/73855373/176022721-b28758c9-ca49-4b68-a419-50bd6e56527e.png">

1. Vul-Scope collects a reference trace and a target trace.
2. We perform cross-version trace alignment, which put simply aligns the code so that it performs the same functions. 
3. If a crash is observed, Vul-Scope verifies whether the crash was triggered by a vulnerability. 
4. Alternatively, based on the aligned cross-version traces, Vul-Scope identifies the critical variables that caused the crash.

### Results
After conducting experiments on 30 CVEs (commmon vulnerabilities and exposures) on 470 versions of software, it was found the VulScope results in no false positives and only 7.9% false negatives. When compared to other methods solving the same issue, VulScope signficantly outperforms. 
