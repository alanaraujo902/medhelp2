'use client';

import { forwardRef, createContext, useContext } from 'react';
import { cn } from '@/lib/utils';

interface RadioGroupContextValue {
  name: string;
  value: string;
  onChange: (value: string) => void;
  disabled?: boolean;
}

const RadioGroupContext = createContext<RadioGroupContextValue | null>(null);

interface RadioGroupProps {
  name: string;
  value: string;
  onChange: (value: string) => void;
  disabled?: boolean;
  className?: string;
  children: React.ReactNode;
}

const RadioGroup = forwardRef<HTMLDivElement, RadioGroupProps>(
  ({ name, value, onChange, disabled, className, children }, ref) => {
    return (
      <RadioGroupContext.Provider value={{ name, value, onChange, disabled }}>
        <div ref={ref} role="radiogroup" className={cn('space-y-2', className)}>
          {children}
        </div>
      </RadioGroupContext.Provider>
    );
  }
);

RadioGroup.displayName = 'RadioGroup';

interface RadioGroupItemProps {
  value: string;
  label: string;
  description?: string;
  disabled?: boolean;
  className?: string;
}

const RadioGroupItem = forwardRef<HTMLInputElement, RadioGroupItemProps>(
  ({ value, label, description, disabled: itemDisabled, className }, ref) => {
    const context = useContext(RadioGroupContext);
    
    if (!context) {
      throw new Error('RadioGroupItem must be used within a RadioGroup');
    }
    
    const { name, value: groupValue, onChange, disabled: groupDisabled } = context;
    const isDisabled = itemDisabled || groupDisabled;
    const isChecked = groupValue === value;
    const inputId = `${name}-${value}`;

    return (
      <label
        htmlFor={inputId}
        className={cn(
          'flex items-start gap-3 cursor-pointer group p-3 rounded-lg border-2 transition-all',
          isChecked
            ? 'border-blue-600 bg-blue-50'
            : 'border-gray-200 hover:border-gray-300 bg-white',
          isDisabled && 'cursor-not-allowed opacity-50',
          className
        )}
      >
        <div className="relative flex-shrink-0 mt-0.5">
          <input
            type="radio"
            id={inputId}
            ref={ref}
            name={name}
            value={value}
            checked={isChecked}
            onChange={() => onChange(value)}
            disabled={isDisabled}
            className="sr-only peer"
          />
          <div
            className={cn(
              'w-5 h-5 border-2 rounded-full transition-all',
              isChecked
                ? 'border-blue-600'
                : 'border-gray-300 group-hover:border-gray-400'
            )}
          />
          <div
            className={cn(
              'absolute top-1 left-1 w-3 h-3 rounded-full bg-blue-600 transition-transform',
              isChecked ? 'scale-100' : 'scale-0'
            )}
          />
        </div>
        <div className="flex flex-col">
          <span className={cn(
            'text-sm font-medium',
            isChecked ? 'text-blue-900' : 'text-gray-900'
          )}>
            {label}
          </span>
          {description && (
            <span className={cn(
              'text-sm',
              isChecked ? 'text-blue-700' : 'text-gray-500'
            )}>
              {description}
            </span>
          )}
        </div>
      </label>
    );
  }
);

RadioGroupItem.displayName = 'RadioGroupItem';

export { RadioGroup, RadioGroupItem };
