---
tags:
- RequirementType
title: REQUIREMENT_CITY_IS_OWNER_CAPITAL_CONTINENT
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_CITY_IS_OWNER_CAPITAL_CONTINENT
>
> * Class: `CITIES`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRES_CITY_IS_NOT_OWNER_CAPITAL_CONTINENT"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType,
		Inverse
	)
VALUES
	(
		"REQUIRES_CITY_IS_NOT_OWNER_CAPITAL_CONTINENT",
		"REQUIREMENT_CITY_IS_OWNER_CAPITAL_CONTINENT",
		1
	);


```
