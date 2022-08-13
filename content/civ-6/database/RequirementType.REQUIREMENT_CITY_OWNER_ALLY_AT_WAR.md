---
tags:
- RequirementType
title: REQUIREMENT_CITY_OWNER_ALLY_AT_WAR
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_CITY_OWNER_ALLY_AT_WAR
>
> * Class: `CITIES`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRES_ALLY_IS_AT_WAR"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_ALLY_IS_AT_WAR",
		"REQUIREMENT_CITY_OWNER_ALLY_AT_WAR"
	);


```
