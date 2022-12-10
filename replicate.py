import replicate

def callDeforumOnReplicate():
    model = replicate.models.get("deforum/deforum_stable_diffusion")
    version = model.versions.get("e22e77495f2fb83c34d5fae2ad8ab63c0a87b6b573b6208e1535b23b89ea66d6")
    output = version.predict(max_frames="30")
    return output