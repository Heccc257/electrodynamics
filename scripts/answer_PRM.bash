version=$1
data_set=$2
model="Qwen2.5-PRM"
python -u answer.py \
    --model $model \
    --data $data_set \
    --output output \
    --prompt none