# TriTrain
Author: Qingkai Zeng (qzeng@nd.edu). EMNLP’20. Adaptive Scientific Named Entity Recognition (NER).

[Tri-Train: Automatic Pre-Fine Tuning between Pre-Training and Fine-Tuning for SciNER](https://www.aclweb.org/anthology/2020.findings-emnlp.429.pdf)  
Authors: Qingkai Zeng (ND), Wenhao Yu (ND), Mengxia Yu (ND), Tianwen Jiang (HIT), Tim Weninger (ND), Meng Jiang (ND)

> This paper proposed a novel framework to introduce a “pre-fine tuning” step between pre-training and fine-tuning to enhance the NER related tasks on scientific domain.

## Requirements
A detailed dependencies list can be found in `requirements.txt` and can be installed by:

```
  pip install -r requirements.txt
```

## Example of distant corpus
There are two files for labeled distant corpus. One is `train.txt` which contains the sentences used in pre-fine-tuining. The other one is `train.dist` which contains the position of the automatically labeled concepts.

> `train.txt` : We used neural network as a machine learning method.  
> `train.dist` : 0 0 1 1 0 0 1 1 0 0

## Pre-Fine-tune a BERT model

```
  cd language_model
  sh run_lm.sh
```

## Fine-tuning a NER model

Please put the BERT-based model after pre-fine-tuning in the `./NER_model/PFT` and update the parameters in `./NER_model/configs`. 
```
  cd NER_model
  sh train_local.sh
```

## Reference
```
@inproceedings{zeng2020tri,
  title={Tri-Train: Automatic Pre-Fine Tuning between Pre-Training and Fine-Tuning for SciNER},
  author={Zeng, Qingkai and Yu, Wenhao and Yu, Mengxia and Jiang, Tianwen and Weninger, Tim and Jiang, Meng},
  booktitle={Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing: Findings},
  pages={4778--4787},
  year={2020}
}
```
