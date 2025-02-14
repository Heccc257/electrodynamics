version=$1
data_set=$2
# model="DeepSeek-Elec-v"$version
model="DeepSeek-Elec-v"$version
python -u answer_cot.py \
    --model DeepSeek-Elec-full \
    --data $data_set \
    --output output