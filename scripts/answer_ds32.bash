data_set=$1
model="DeepSeek-Elec-32B"
python -u answer_ref.py \
    --model $model \
    --data $data_set \
    --output output