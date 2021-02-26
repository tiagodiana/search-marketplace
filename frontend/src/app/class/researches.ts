import {Product} from './product';

export class Researches
{
  id: number;
  ip_address: string;
  query: string;
  result: Product[];
  site: string;
  type: string;
  create_date: any;
  update_date: any;

  constructor(
    id: number = 0,
    ip_address: string = '',
    query: string = '',
    result: Product[] = [],
    site: string = '',
    type: string = '',
    create_date: any = '',
    update_date: any = '',
  )
  {
    this.id = id;
    this.ip_address = ip_address;
    this.query = query;
    this.result = result;
    this.site = site;
    this.type = type;
    this.create_date = create_date;
    this.update_date = update_date;
  }

}
