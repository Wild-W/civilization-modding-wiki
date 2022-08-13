---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_AT_WAR_AND_HAS_MET
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_AT_WAR_AND_HAS_MET
>
> * Class: `PLAYERS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRES_AT_WAR_AND_HAS_MET"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType,
		Inverse
	)
VALUES
	(
		"REQUIRES_AT_WAR_AND_HAS_MET",
		"REQUIREMENT_PLAYER_AT_WAR_AND_HAS_MET",
		1
	);

```
