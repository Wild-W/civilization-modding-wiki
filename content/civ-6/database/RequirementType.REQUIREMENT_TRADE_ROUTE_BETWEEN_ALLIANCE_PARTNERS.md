---
tags:
- RequirementType
title: REQUIREMENT_TRADE_ROUTE_BETWEEN_ALLIANCE_PARTNERS
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_TRADE_ROUTE_BETWEEN_ALLIANCE_PARTNERS
>
> * Class: `TRADE ROUTES`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRES_TRADE_ROUTE_BETWEEN_ALLIES"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_TRADE_ROUTE_BETWEEN_ALLIES",
		"REQUIREMENT_TRADE_ROUTE_BETWEEN_ALLIANCE_PARTNERS"
	);


```
