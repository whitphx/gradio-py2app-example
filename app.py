import logging
import time

import webview

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def wait_for_url(url: str, max_retries: int = 30, retry_interval: int = 1):
    import urllib.request
    import urllib.error

    for _ in range(max_retries):
        try:
            urllib.request.urlopen(url)
            break
        except urllib.error.URLError:
            time.sleep(retry_interval)
    else:
        raise Exception(f"Failed to connect to {url} after {max_retries * retry_interval} seconds")


logger.info("Starting Gradio app")
# Launching the Gradio app script in a separate process doesn't work.
# 1. When using `subprocess.Popen([sys.executable, app_script])`,
#    the `gradio` package is not found in the subprocess.
# 2. When using `multiprocessing.Process(target=gradio_app_runner)`,
#    the following error occurs:
#    ```
#    unknown option --multiprocessing-fork
#    usage: /<project-root>/dist/pywebview-desktop-trial.app/Contents/MacOS/python [option] ... [-c cmd | -m mod | file | -] [arg] ...
#    ```

from gradio_app import demo
demo.launch(prevent_thread_lock=True)

gradio_url = "http://localhost:7860/"

wait_for_url(gradio_url)

logger.info("Starting webview")
webview.create_window('Hello world', gradio_url)
webview.start(debug=True)

logger.info("Terminating Gradio app")
# p.terminate()
# gradio_app.join()
