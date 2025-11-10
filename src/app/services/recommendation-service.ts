import { inject, Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';

export interface Gasto {
  category: string;
  amount: number;
}

export interface Product {
  id: number;
  name: string;
  categories: Gasto[]
}

@Injectable({
  providedIn: 'root',
})

export class RecommendationService {

  private http = inject(HttpClient);

  // URL de una API de prueba
  private apiUrl = '/recommendedProducts';

  getPosts(): Observable<Product[]> {
    return this.http.get<Product[]>(this.apiUrl);
  }

  getPostById(id: number): Observable<Product> {
    return this.http.get<Product>(`${this.apiUrl}/${id}`);
  }
}