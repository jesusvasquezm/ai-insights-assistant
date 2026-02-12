import { useState } from "react";
import { analyzeText } from "./services/api";

function App() {
  const [text, setText] = useState<string>("");
  const [response, setResponse] = useState<string>("");
  const [loading, setLoading] = useState<boolean>(false);

  const handleSubmit = async () => {
    try {
      setLoading(true);

      const result = await analyzeText({ text });
      setResponse(result.analysis);

    } catch (error) {
      console.error(error);
      setResponse("Error analyzing text.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: 40 }}>
      <h1>AI Insights Assistant</h1>

      <textarea
        rows={6}
        value={text}
        onChange={(e) => setText(e.target.value)}
      />

      <br />

      <button onClick={handleSubmit} disabled={loading}>
        {loading ? "Analyzing..." : "Analyze"}
      </button>

      <h2>Response:</h2>
      <p>{response}</p>
    </div>
  );
}

export default App;
