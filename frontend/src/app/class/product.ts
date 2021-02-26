export class Product
{
  description: string;
  link: string;
  photo: string;
  price: string;
  merchant: any;

  constructor(
    description: string = '',
    link: string = '',
    photo: string = '',
    price: string = '',
    merchant: any = false
  )
  {
    this.description = description;
    this.link = link;
    this.photo = photo;
    this.price = price;
    this.merchant = merchant;
  }
}
