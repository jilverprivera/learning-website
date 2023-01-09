import { CategoryType } from "./categoryType";

export type SubCategoryType = {
  uuid:       string;
  name:       string;
  slug:       string;
  principal:  CategoryType;
  created_at: string;
}