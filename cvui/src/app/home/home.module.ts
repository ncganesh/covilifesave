import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { HomeRoutingModule } from './home-routing.module';
import { HomeComponent } from './home.component';

import { ChartModule } from 'angular-highcharts';
import { MaterialModule } from '../material.module';
import { GraphQLModule } from '../graphql.module';

@NgModule({
  declarations: [
    HomeComponent
  ],
  imports: [
    CommonModule,
    HomeRoutingModule,
    ChartModule,
    MaterialModule,
    GraphQLModule
  ]
})
export class HomeModule { }
