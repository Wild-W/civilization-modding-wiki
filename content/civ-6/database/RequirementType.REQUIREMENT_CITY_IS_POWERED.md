---
tags:
- RequirementType
title: REQUIREMENT_CITY_IS_POWERED
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_CITY_IS_POWERED
>
> * Class: `CITIES`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRES_CITY_IS_POWERED"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_CITY_IS_POWERED",
		"REQUIREMENT_CITY_IS_POWERED"
	);

```
