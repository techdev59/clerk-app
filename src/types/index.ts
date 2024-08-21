import { ReactNode } from "react";

export interface ChildrenProps {
  children?: ReactNode;
}

export interface SelectItemProps {
  label: string;
  value: string | number | undefined;
}

export interface SelectDropdownProps extends InputProps {
  options: SelectItemProps[];
}

export interface InputProps extends ChildrenProps {
  label: string;
  error?: string;
  id: string;
  [key: string]: any;
}

export interface SiteAddProps {
  cluster_id: number;
  taskdefinition_name: string;
  domain_name: string;
  sub_domain: boolean;
  container_name: string;
  container_image_url: string;
}
export interface RecordAddProps {
  record_name?: string;
  record_type: string;
  record_value: string;
  ttl: number;
}

export interface DomainAddProps {
  domain_name: string;
  sub_domain: string | boolean;
}

export interface TaskIDProps {
  task_definition_id: number;
}

export interface ResetWPUserPassword {
  email: string;
}
