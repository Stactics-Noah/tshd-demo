"""
Very small view that:
  * Shows the form and any prior chat history on GET
  * Handles the user message and calls Azure OpenAI on POST
  * Stores the running conversation in the Django session
"""
import os
from django.shortcuts import render, redirect
from .forms import ChatForm

# ------------  OPENAI v1 + AZURE SET-UP  ------------------------
from openai import AzureOpenAI   # new in v1

# Find this information in the Azure Portal: go to https://ai.azure.com/resource/deployments/ and click on your deployment
client = AzureOpenAI(
    api_key=os.environ["AZURE_OPENAI_KEY"],  # set in your environment
    azure_endpoint="https://noahb-m9wmmlqt-eastus2.cognitiveservices.azure.com/",
    api_version="2024-12-01-preview",
)
# ----------------------------------------------------------------

SYSTEM_PROMPT = \
"""
Human: You are an AI assistant for a demonstration of the Azure OpenAI service. You must always respond in a helpful and friendly manner.
"""

def chat_view(request):
    history = request.session.get("history", [])

    if request.method == "POST":
        form = ChatForm(request.POST)
        if form.is_valid():
            user_msg = form.cleaned_data["message"]
            history.append({"role": "user", "content": user_msg})

            try:
                response = client.chat.completions.create(
                    model='gpt-4o-mini-tshd-demo',   # not the “model family” but your deployment name
                    messages=[{"role": "system", "content": SYSTEM_PROMPT},] + history,
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

def reset_chat(request):
    """
    Wipes the in-session chat history and returns the user to the main page.
    """
    request.session.pop("history", None)     # quietly remove the key if present
    return redirect("chat:index")