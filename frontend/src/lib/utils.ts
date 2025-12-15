import { type ClassValue, clsx } from "clsx";
import { twMerge } from "tailwind-merge";

/**
 * Combina classes CSS com suporte a Tailwind merge
 */
export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

/**
 * Formata data para exibição
 */
export function formatDate(date: string | Date, format: string = 'DD/MM/YYYY'): string {
  const d = new Date(date);
  const day = String(d.getDate()).padStart(2, '0');
  const month = String(d.getMonth() + 1).padStart(2, '0');
  const year = d.getFullYear();
  
  return format
    .replace('DD', day)
    .replace('MM', month)
    .replace('YYYY', String(year))
    .replace('YY', String(year).slice(-2));
}

/**
 * Delay helper para async/await
 */
export function delay(ms: number): Promise<void> {
  return new Promise(resolve => setTimeout(resolve, ms));
}

/**
 * Capitaliza primeira letra
 */
export function capitalize(str: string): string {
  return str.charAt(0).toUpperCase() + str.slice(1);
}

/**
 * Converte texto para o formato de título especificado
 */
export function formatTitle(text: string, format: 'maiusculas' | 'primeira_maiuscula' | 'minusculas'): string {
  switch (format) {
    case 'maiusculas':
      return text.toUpperCase();
    case 'primeira_maiuscula':
      return text.charAt(0).toUpperCase() + text.slice(1).toLowerCase();
    case 'minusculas':
      return text.toLowerCase();
    default:
      return text;
  }
}
