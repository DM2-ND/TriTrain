# TriTrain

[Tri-Train: Automatic Pre-Fine Tuning between Pre-Training and Fine-Tuning for SciNER](https://www.aclweb.org/anthology/2020.findings-emnlp.429.pdf)
Authors: Qingkai Zeng (ND), Wenhao Yu (ND), Mengxia Yu (ND), Tianwen Jiang (HIT), Tim Weninger (ND), Meng Jiang (ND)

> This paper proposed a novel framework to introduce a “pre-fine tuning” step between pre-training and fine-tuning to enhance the NER related tasks on scientific domain.

# Pre-Fine-tune a BERT model using `run_lm.py`

```bash
  python run_lm.py --model_type bert --model_name_or_path MODEL_NAME\
   --do_train --train_data_file train.txt --train_dist_file train.dist\
   --do_eval --eval_data_file eval.txt --eval_pos_file eval.dist\
   --mlm --mlm_probability 0.15 --line_by_line --num_train_epochs 50 --warmup_steps 750\
   --logging_steps 750 --save_steps 750 --eval_all_checkpoints --per_gpu_train_batch_size 8\
   --gradient_accumulation_steps 2 --per_gpu_eval_batch_size 16 --learning_rate 5e-5  --output_dir OUTPUT_DIR
```

where `OUTPUT_DIR` should be the directory to store the saved models.

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
