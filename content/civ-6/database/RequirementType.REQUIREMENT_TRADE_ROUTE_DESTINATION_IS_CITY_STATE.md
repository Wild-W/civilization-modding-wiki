---
tags:
- RequirementType
title: REQUIREMENT_TRADE_ROUTE_DESTINATION_IS_CITY_STATE
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_TRADE_ROUTE_DESTINATION_IS_CITY_STATE
>
> * Class: `TRADE ROUTES`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRES_TRADE_ROUTE_TO_CITY_STATE"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_TRADE_ROUTE_TO_CITY_STATE",
		"REQUIREMENT_TRADE_ROUTE_DESTINATION_IS_CITY_STATE"
	);


```
