import { BrandType } from "./brandType";
import { CommentType } from "./commentType";
import { SubCategoryType } from "./subCategoryType";

export type ProductType = {
  uuid:              string;
  title:             string;
  slug:              string;
  category:          SubCategoryType;
  brand:             BrandType;
  short_description: string;
  content:           string;
  price:             string;
  compare_price:     string;
  stock:             number;
  sold:              number;
  image:             string;
  thumbnail:         string;
  comment:           CommentType[];
  stars:             number;
  total_stars:       number;
  best_seller:       boolean;
  status:            string;
  created_at:        string;
}