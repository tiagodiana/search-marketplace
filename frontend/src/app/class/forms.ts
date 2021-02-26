export class FormSearch
{
  site: string;
  category: string;
  type: string;
  query: string;

  constructor(
    site: string = '',
    category: string = '',
    type: string = '',
    query: string = '')
  {
    this.site = site;
    this.category = category;
    this.type = type;
    this.query = query;
  }
}
