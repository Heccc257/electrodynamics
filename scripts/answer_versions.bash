version=$1
model="Qwen2.5-Math-7B-Elec-v"$version
echo $model
python -u answer.py \
    --model $model \
    --data datasets/电动力学习题解答.json \
    --output output