import { Component, OnInit } from '@angular/core';
import {ApiServiceService} from '../services/api-service.service';
import {Researches} from '../class/researches';
import {Observable} from 'rxjs';

@Component({
  selector: 'app-history',
  templateUrl: './history.component.html',
  styleUrls: ['./history.component.css']
})
export class HistoryComponent implements OnInit {

  researches: Researches[];
  researches$: Observable<Researches[]>;

  eventGet$: Observable<boolean>;

  loading: boolean;

  constructor(private service: ApiServiceService)
  {
    this.loading = false;
    this.researches = [];
    this.researches$ = new Observable<Researches[]>();
    this.eventGet$ = new Observable<boolean>();
  }

  ngOnInit(): void
  {
    this.eventGet$ = ApiServiceService.emitLoading;
    this.eventGet$.subscribe(data => {
      this.loading = data;
    });
    this.get();
  }

  get(): void
  {
    this.researches$ = this.service.getResearches();
  }

}
