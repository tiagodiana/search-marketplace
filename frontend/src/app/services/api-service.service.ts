import {EventEmitter, Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {environment} from '../../environments/environment';
import {Observable} from 'rxjs';
import {take, tap} from 'rxjs/operators';
import {Product} from '../class/product';

@Injectable({
  providedIn: 'root'
})
export class ApiServiceService {

  static emitLoading = new EventEmitter<boolean>();
  private url: string;
  private options: any;



  constructor(private http: HttpClient)
  {
    this.url = environment.urlApi;
    this.options = {
      headers: new HttpHeaders({
        accept: 'application/json',
      }),
      params: {}
    };
  }

  getQueryMarketplace(query: any): Observable<Product[]>
  {
    ApiServiceService.emitLoading.emit(true);
    return this.http.post<Product[]>(`${this.url}/queryMarketplace`, query).pipe(
      tap(
        (event) => {
            ApiServiceService.emitLoading.emit(false);
          }
      )
    );
  }


}
