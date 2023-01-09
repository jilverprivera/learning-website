import useSWR from "swr";

export const useData = (url: string) => {

  const fetcher = (args: string) =>
    fetch(args).then((res): Promise<any> => res.json());
  const { data, error, isLoading } = useSWR(url, fetcher);
  
  return { data, error, isLoading };
};
