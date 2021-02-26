import {Product} from './product';

export class Result
{
  id: number;
  result: Product[];

  constructor(
    id: number = 0,
    result: Product[] = []
  )
  {
    this.id = id;
    this.result = result;
  }
}
