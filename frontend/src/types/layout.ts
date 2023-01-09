export type layout = {
  children: JSX.Element | JSX.Element[];
  title: string;
};

export type childrenProps = {
  children: JSX.Element | JSX.Element[];
};

export type navLinkTypes = {
  first?: boolean;
  last?: boolean;
  extras?: string;
  icon?: JSX.Element | JSX.Element[];
  title: string;
  route: string;
};

export type navLinkType = {
  label: string;
  path: string;
  last?: boolean;
  first?: boolean;
};
