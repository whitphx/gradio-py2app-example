## PyInstaller

```shell
$ uv run pyinstaller app.py \
    --collect-data gradio \
    --collect-data gradio_client \
    --additional-hooks-dir=./hooks \
    --runtime-hook ./runtime_hooks/gradio_hook.py
```

## py2app

```shell
$ uv run setup.py py2app -A
```
