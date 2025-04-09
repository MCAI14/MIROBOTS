async function checkForUpdates() {
    const updateUrl = "https://mirobots.netlify.app/update.json";

    try {
        const response = await fetch(updateUrl);
        const data = await response.json();

        const currentVersion = "1.0.0"; // Versão atual do sistema
        if (data.latestVersion !== currentVersion) {
            console.log(`New update found: Version ${data.latestVersion}`);
            
            // Notifica o usuário sobre a atualização
            alert(`A new update is available: Version ${data.latestVersion}\n\nChangelog:\n${data.changelog}`);
            
            // Baixa automaticamente o arquivo de atualização
            const downloadResponse = await fetch(data.downloadUrl);
            const blob = await downloadResponse.blob();

            // Salva o arquivo localmente
            const a = document.createElement("a");
            a.href = URL.createObjectURL(blob);
            a.download = "mirobots-update.zip";
            a.click();

            alert("The update has been downloaded. Please install it manually.");
        } else {
            console.log("Your system is up to date!");
        }
    } catch (error) {
        console.error("Error checking for updates:", error);
        alert("Unable to check for updates. Please try again later.");
    }
}

// Call the function when the page loads
document.addEventListener("DOMContentLoaded", checkForUpdates);