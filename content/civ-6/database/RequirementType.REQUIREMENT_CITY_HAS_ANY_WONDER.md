---
tags:
- RequirementType
title: REQUIREMENT_CITY_HAS_ANY_WONDER
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_CITY_HAS_ANY_WONDER
>
> * Class: `CITIES`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRES_CITY_HAS_WONDER"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_CITY_HAS_WONDER",
		"REQUIREMENT_CITY_HAS_ANY_WONDER"
	);


```
