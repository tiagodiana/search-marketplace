import { Component, OnInit } from '@angular/core';
import {ApiServiceService} from '../services/api-service.service';
import {Observable} from 'rxjs';
import {FormSearch} from '../class/forms';
import {Product} from '../class/product';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  searchForm: FormSearch;
  queryRequest$: Observable<Product[]>;

  eventSearch$: Observable<boolean>;


  products: Product[];

  clickCancel: boolean;
  validate: boolean;

  loading: boolean;


  constructor(
    private service: ApiServiceService
  )
  {
    this.searchForm = new FormSearch();
    this.queryRequest$ = new Observable<any>();
    this.products = [];
    this.validate = false;
    this.clickCancel = false;
    this.eventSearch$ = new Observable<boolean>();
    this.loading = false;
  }


  ngOnInit(): void
  {
    this.eventSearch$ = ApiServiceService.emitLoading;
    this.eventSearch$.subscribe(data => {
      this.loading = data;
      this.clickCancel = data;
    });
  }


  changeSite(): void
  {
    this.validate = false;
  }

  changeCategory(): void
  {
    this.validate = false;
    this.searchForm.type = 'cat';
    this.requestSearch();
    this.clickCancel = false;
  }



  getQueryMarketplace(): void
  {
    this.searchForm.type = 'qry';
    this.validate = false;
    if (!this.searchForm.site)
    {
      this.validate = true;
      return;
    }

    if (!this.searchForm.query)
    {
      this.validate = true;
      return;
    }

    this.requestSearch();
  }

  requestSearch(): void
  {
    this.queryRequest$ = this.service.getQueryMarketplace(this.searchForm);
  }


}
