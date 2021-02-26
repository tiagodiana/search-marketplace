import { Component, OnInit } from '@angular/core';
import {Product} from '../class/product';
import {Result} from '../class/result';
import {Observable} from 'rxjs';
import {ApiServiceService} from '../services/api-service.service';
import {ActivatedRoute} from '@angular/router';

@Component({
  selector: 'app-result',
  templateUrl: './result.component.html',
  styleUrls: ['./result.component.css']
})
export class ResultComponent implements OnInit {

  result: Result;
  result$: Observable<Result>;

  eventApi$: Observable<boolean>;

  validate: boolean;

  id: string;

  loading: boolean;

  constructor(
    private service: ApiServiceService,
    private routerActive: ActivatedRoute)
  {
    this.result = new Result();
    this.result$ = new Observable<Result>();
    this.eventApi$ = new Observable<boolean>();
    this.validate = false;
    this.id = this.routerActive.snapshot.params[`id`];
    this.loading = false;
  }

  ngOnInit(): void
  {
    this.eventApi$ = ApiServiceService.emitLoading;
    this.eventApi$.subscribe(data => {
      this.loading = data;
    });
    this.get();
  }

  get(): void
  {
    this.result$ = this.service.getResearchesId(this.id);
  }
}
