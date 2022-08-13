---
tags:
- RequirementType
title: REQUIREMENT_CITY_HAS_FULL_LOYALTY
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_CITY_HAS_FULL_LOYALTY
>
> * Class: `CITIES`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRES_FULL_LOYALTY"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_FULL_LOYALTY",
		"REQUIREMENT_CITY_HAS_FULL_LOYALTY"
	);


```
