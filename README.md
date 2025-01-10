## answer

用于批量回答问题的脚本

### 使用方法

* 使用前先创建`config`目录，填入`model2path.json`和`prompt.json`文件

  * 例子：

    * 

    ```json
    // model2path.json
    
    {
        "Qwen2-1.5B-Instruct": "~/models/hub/Qwen/Qwen2-1.5B-Instruct",
        "Qwen2.5-14B-Instruct": "/lustre/home/2401210610/models/hub/Qwen/Qwen2.5-14B-Instruct"
    }
    ```

    * 

    ```json
    // prompt.json
    
    {
        "default": "你是一位电动力学领域的专家，请解答下面的电动力学问题，给出latex的公式形式: {input}"
    }
    ```

* 运行`answer.py`脚本
  * 参数形式可以看`scripts/example_anser.bash`里面的例子
  * 运行示例：`bash scripts/example_anser.bash`