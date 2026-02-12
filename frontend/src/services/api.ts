import axios from "axios";
import type { AnalyzeRequest, AnalyzeResponse } from "../types/analyse";


const api = axios.create({
  baseURL: "http://127.0.0.1:8000",
});

export const analyzeText = async (
  data: AnalyzeRequest
): Promise<AnalyzeResponse> => {
  const response = await api.post<AnalyzeResponse>("/analyze", data);
  return response.data;
};
