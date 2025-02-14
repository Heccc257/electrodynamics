data_set=$1
model="DeepSeek-Elec-full"
python -u answer_dpo.py \
    --model $model \
    --data $data_set \
    --output output