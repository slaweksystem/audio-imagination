import replicate

def loadSecrets():
    secrets = {}
    with open ("secrets.txt", 'r') as f:
         for line in f:
            key, value = line.strip().split('=')
            secrets[key] = value
    return secrets

def initializeReplicateClient(secrets):
    client = replicate.Client(api_token=secrets["REPLICATE_API_TOKEN"])
    return client

def callDeforumOnReplicate(client, max_frames=100, prompt="a beautiful portrait of a woman by Artgerm, trending on Artstation",
angle="0:(0)", zoom="0: (1.04)", translation_x="0: (0)", translation_y="0: (0)", color_coherence="Match Frame 0 LAB",
sampler="plms", fps=15, seed=None):
    model = client.models.get("deforum/deforum_stable_diffusion")
    version = model.versions.get("e22e77495f2fb83c34d5fae2ad8ab63c0a87b6b573b6208e1535b23b89ea66d6")
    output = version.predict(max_frames, prompt, angle, zoom, translation_x, translation_y,
    color_coherence, sampler, fps, seed)
    return output

if __name__ == "__main__":
    secrets = loadSecrets()
    client = initializeReplicateClient(secrets)
    print(callDeforumOnReplicate(client))