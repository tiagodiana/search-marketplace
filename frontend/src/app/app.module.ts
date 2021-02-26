import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import {HttpClientModule} from '@angular/common/http';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import {FormsModule} from '@angular/forms';
import { LoadingComponent } from './loading/loading.component';
import { HistoryComponent } from './history/history.component';
import { ResultComponent } from './result/result.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    LoadingComponent,
    HistoryComponent,
    ResultComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    NgbModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
