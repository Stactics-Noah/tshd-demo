"""
Very small view that:
  * Shows the form and any prior chat history on GET
  * Handles the user message and calls Azure OpenAI on POST
  * Stores the running conversation in the Django session
"""
# import os
from django.shortcuts import render, redirect
from .forms import ChatForm

# ------------  OPENAI v1 + AZURE SET-UP  ------------------------
from openai import AzureOpenAI   # new in v1

# Find this information in the Azure Portal: go to https://ai.azure.com/resource/deployments/ and click on your deployment
client = AzureOpenAI(
    api_key="<your-azure-api-key>",                              # your key  🔑
    azure_endpoint="<your-deployment-endpoint>",                 # your endpoint 🌐
    api_version="2024-12-01-preview",                            # same version you use in Portal
)
DEPLOYMENT_NAME = "<deployment-name>"   # the *deployment name* you set in the Portal. NOT the model name!
# ----------------------------------------------------------------

def chat_view(request):
    history = request.session.get("history", [])

    if request.method == "POST":
        form = ChatForm(request.POST)
        if form.is_valid():
            user_msg = form.cleaned_data["message"]
            history.append({"role": "user", "content": user_msg})

            try:
                response = client.chat.completions.create(
                    model=DEPLOYMENT_NAME,   # not the “model family” but your deployment name
                    messages=history,
                )
                assistant_msg = response.choices[0].message.content.strip()
            except Exception as exc:
                assistant_msg = f"(error talking to Azure OpenAI: {exc})"

            history.append({"role": "assistant", "content": assistant_msg})
            request.session["history"] = history
            request.session.modified = True
            return redirect("chat:index")
    else:
        form = ChatForm()

    return render(request, "chat/index.html", {"form": form, "history": history})
