import os
import subprocess
import pickle
import yaml


def run_maintenance(task_name, args):
    command = "python scripts/" + task_name + ".py " + " ".join(args)
    return os.popen(command).read()  # CWE-78


def ping_host(host):
    return subprocess.check_output("ping -c 1 " + host, shell=True)  # CWE-78


def load_job_state(blob):
    return pickle.loads(blob)  # CWE-502


def load_yaml_config(text):
    return yaml.load(text, Loader=yaml.Loader)  # CWE-502


def evaluate_rule(rule, context):
    return eval(rule, {}, context)  # CWE-94
