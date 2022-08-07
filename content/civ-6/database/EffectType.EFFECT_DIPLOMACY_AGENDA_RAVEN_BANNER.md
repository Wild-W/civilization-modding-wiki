---
tags:
- EffectType
title: EFFECT_DIPLOMACY_AGENDA_RAVEN_BANNER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_DIPLOMACY_AGENDA_RAVEN_BANNER
>
> * Class: `PLAYERS`
> * Parameters:
>	* BottomPercentage `Integer`
>	* BottomRankingDiploMod `Integer`
>	* StatementKey `String`
>	* TopPercentage `Integer`
>	* TopRankingDiploMod `Integer`

## Samples

```SQL {title="AGENDA_RAVEN_BANNER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		OwnerRequirementSetId,
		SubjectRequirementSetId
	)
VALUES
	(
		"AGENDA_RAVEN_BANNER",
		"MODIFIER_PLAYER_DIPLOMACY_AGENDA_RAVEN_BANNER",
		"ON_TURN_STARTED",
		"PLAYER_IS_MAJOR_CIV_KNOWN_10_TURNS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"AGENDA_RAVEN_BANNER",
		"BottomPercentage",
		30
	),
	(
		"AGENDA_RAVEN_BANNER",
		"BottomRankingDiploMod",
		"-8"
	),
	(
		"AGENDA_RAVEN_BANNER",
		"StatementKey",
		"AGENDA_RAVEN_BANNER_WARNING"
	),
	(
		"AGENDA_RAVEN_BANNER",
		"TopPercentage",
		65
	),
	(
		"AGENDA_RAVEN_BANNER",
		"TopRankingDiploMod",
		8
	);
	
```

