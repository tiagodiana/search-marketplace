import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {HomeComponent} from './home/home.component';
import {HistoryComponent} from './history/history.component';
import {ResultComponent} from './result/result.component';

const routes: Routes = [
  {path: '', component: HomeComponent},
  {path: 'home', redirectTo: '/'},
  {path: 'history', component: HistoryComponent},
  {path: 'result/:id', component: ResultComponent},


  {path: '*', redirectTo: '/'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
