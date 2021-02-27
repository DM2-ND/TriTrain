python run_lm.py --model_type bert --model_name_or_path MODEL_NAME\
   --do_train --train_data_file train.txt --train_dist_file train.dist\
   --do_eval --eval_data_file eval.txt --eval_pos_file eval.dist\
   --mlm --mlm_probability 0.15 --line_by_line --num_train_epochs 50 --warmup_steps 750\
   --logging_steps 750 --save_steps 750 --eval_all_checkpoints --per_gpu_train_batch_size 8\
   --gradient_accumulation_steps 2 --per_gpu_eval_batch_size 16 --learning_rate 5e-5  --output_dir OUTPUT_DIR