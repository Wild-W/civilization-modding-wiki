---
tags:
- RequirementType
title: REQUIREMENT_ALLIANCE_AT_WAR_WITH_COMBAT_TARGET
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_ALLIANCE_AT_WAR_WITH_COMBAT_TARGET
>
> * Class: `PLAYERS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRES_ALLIES_AT_WAR_WITH_TARGET"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_ALLIES_AT_WAR_WITH_TARGET",
		"REQUIREMENT_ALLIANCE_AT_WAR_WITH_COMBAT_TARGET"
	);

```
