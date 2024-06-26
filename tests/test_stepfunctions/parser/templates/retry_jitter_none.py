retry_template_jitter_none = {
    "Comment": "RETRY_INTERVAL_FEATURES_JITTER_NONE",
    "StartAt": "LambdaTask",
    "States": {
        "LambdaTask": {
            "Type": "Task",
            "Resource": "_tbd_",
            "End": True,
            "Retry": [
                {
                    "Comment": "Includes all retry langauge features with JitterStrategy NONE.",
                    "ErrorEquals": ["States.ALL"],
                    "IntervalSeconds": 1,
                    "MaxAttempts": 2,
                    "BackoffRate": 1,
                    "MaxDelaySeconds": 3,
                    "JitterStrategy": "NONE",
                }
            ],
        }
    },
}
