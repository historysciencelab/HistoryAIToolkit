from rich.console import Console


console = Console()

try:
    import clarifai_grpc
except ImportError:
    clarifai_grpc = None

# # Securely get your credentials
# TODO: Pass in arguments or use env vars
CLARIFAI_PAT = ""
# Specify the correct user_id/app_id pairings
# Since you're making inferences outside your app's scope
CLARIFAI_USER_ID = "meta"
CLARIFAI_APP_ID = "Llama-2"
# Change these to whatever model and text URL you want to use
CLARIFAI_MODEL_ID = "llama2-70b-chat"
CLARIFAI_MODEL_VERSION_ID = "acba9c1995f8462390d7cb77d482810b"


def generate_questions_from_transcript(transcript: str):
    if clarifai_grpc is None:
        console.print(
            "Please install clarifai-grpc: pip install 'historyaitoolkit\[clarifai]'",
            style="bold red",
        )
        exit(1)
    channel = clarifai_grpc.channel.clarifai_channel.ClarifaiChannel.get_grpc_channel()
    stub = clarifai_grpc.grpc.api.service_pb2_grpc.V2Stub(channel)

    metadata = (("authorization", "Key " + CLARIFAI_PAT),)
    userDataObject = clarifai_grpc.grpc.api.resources_pb2.UserAppIDSet(
        user_id=CLARIFAI_USER_ID, app_id=CLARIFAI_APP_ID
    )

    post_model_outputs_response = stub.PostModelOutputs(
        clarifai_grpc.grpc.api.service_pb2.PostModelOutputsRequest(
            user_app_id=userDataObject,
            model_id=CLARIFAI_MODEL_ID,
            version_id=CLARIFAI_MODEL_VERSION_ID,
            inputs=[
                clarifai_grpc.grpc.api.resources_pb2.Input(
                    data=clarifai_grpc.grpc.api.resources_pb2.Data(
                        text=clarifai_grpc.grpc.api.resources_pb2.Text(raw=transcript)
                    )
                )
            ],
        ),
        metadata=metadata,
    )

    if (
        post_model_outputs_response.status.code
        != clarifai_grpc.grpc.api.status.status_code_pb2.SUCCESS
    ):
        print(post_model_outputs_response.status)
        status = post_model_outputs_response.status.description
        raise Exception(f"Post model outputs failed, status: {status}")

    output = post_model_outputs_response.outputs[0]
    return output.data.text.raw
