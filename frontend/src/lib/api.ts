import axios from 'axios';
import type {
  EvolutionTemplate,
  TemplateListResponse,
  PresetTemplatesResponse,
  ConfigurationOptions,
  GeneratedEvolution,
  EvolutionGenerateRequest,
  HealthCheckResponse,
} from '@/types';

/**
 * Cliente API para comunicação com o Backend FastAPI
 */
const api = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api/v1',
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 60000, // 60 segundos para geração de evolução
});

// ============================================
// Templates
// ============================================

export async function getTemplates(): Promise<TemplateListResponse> {
  const response = await api.get<TemplateListResponse>('/templates');
  return response.data;
}

export async function getPresetTemplates(): Promise<PresetTemplatesResponse> {
  const response = await api.get<PresetTemplatesResponse>('/templates/presets');
  return response.data;
}

export async function getUserTemplates(): Promise<TemplateListResponse> {
  const response = await api.get<TemplateListResponse>('/templates/user');
  return response.data;
}

export async function getTemplate(id: string): Promise<EvolutionTemplate> {
  const response = await api.get<EvolutionTemplate>(`/templates/${id}`);
  return response.data;
}

export async function getDefaultTemplate(): Promise<EvolutionTemplate> {
  const response = await api.get<EvolutionTemplate>('/templates/default');
  return response.data;
}

export async function createTemplate(template: Partial<EvolutionTemplate>): Promise<EvolutionTemplate> {
  const response = await api.post<EvolutionTemplate>('/templates', template);
  return response.data;
}

export async function updateTemplate(id: string, template: Partial<EvolutionTemplate>): Promise<EvolutionTemplate> {
  const response = await api.put<EvolutionTemplate>(`/templates/${id}`, template);
  return response.data;
}

export async function deleteTemplate(id: string): Promise<void> {
  await api.delete(`/templates/${id}`);
}

// ============================================
// Evolução
// ============================================

export async function generateEvolution(request: EvolutionGenerateRequest): Promise<GeneratedEvolution> {
  const response = await api.post<GeneratedEvolution>('/evolution/generate', request);
  return response.data;
}

export async function previewEvolution(request: EvolutionGenerateRequest): Promise<GeneratedEvolution> {
  const response = await api.post<GeneratedEvolution>('/evolution/preview', request);
  return response.data;
}

// ============================================
// Opções de Configuração
// ============================================

export async function getConfigurationOptions(): Promise<ConfigurationOptions> {
  const response = await api.get<ConfigurationOptions>('/options');
  return response.data;
}

export async function getContextSubtypes(context: string): Promise<{ context: string; subtypes: Array<{ value: string; label: string }> }> {
  const response = await api.get(`/options/contexts/${context}/subtypes`);
  return response.data;
}

export async function getEvolutionTypes(context: string): Promise<{ context: string; evolution_types: Array<{ value: string; label: string }> }> {
  const response = await api.get(`/options/evolution-types/${context}`);
  return response.data;
}

// ============================================
// Health Check
// ============================================

export async function healthCheck(): Promise<HealthCheckResponse> {
  const response = await api.get<HealthCheckResponse>('/health', {
    baseURL: process.env.NEXT_PUBLIC_API_URL?.replace('/api/v1', '') || 'http://localhost:8000',
  });
  return response.data;
}

export default api;
