---
tags:
- EffectType
title: EFFECT_DIPLOMACY_AGENDA_END_TO_SUFFERING
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_DIPLOMACY_AGENDA_END_TO_SUFFERING
>
> * Class: `PLAYERS`
> * Parameters:
>	* DisappointingHolySitePercentage `Integer`
>	* DisappointingLargeCityPercentage `Integer`
>	* MaxNegativeModifier `Integer`
>	* MaxPositiveModifier `Integer`
>	* StatementKey `String`
>	* TargetHolySitePercentage `Integer`
>	* TargetLargeCityPercentage `Integer`

## Samples

```SQL {title="AGENDA_END_TO_SUFFERING"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		OwnerRequirementSetId,
		SubjectRequirementSetId
	)
VALUES
	(
		"AGENDA_END_TO_SUFFERING",
		"MODIFIER_PLAYER_DIPLOMACY_AGENDA_END_TO_SUFFERING",
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
		"AGENDA_END_TO_SUFFERING",
		"DisappointingHolySitePercentage",
		25
	),
	(
		"AGENDA_END_TO_SUFFERING",
		"DisappointingLargeCityPercentage",
		35
	),
	(
		"AGENDA_END_TO_SUFFERING",
		"MaxNegativeModifier",
		"-8"
	),
	(
		"AGENDA_END_TO_SUFFERING",
		"MaxPositiveModifier",
		8
	),
	(
		"AGENDA_END_TO_SUFFERING",
		"StatementKey",
		"AGENDA_END_TO_SUFFERING_WARNING"
	),
	(
		"AGENDA_END_TO_SUFFERING",
		"TargetHolySitePercentage",
		50
	),
	(
		"AGENDA_END_TO_SUFFERING",
		"TargetLargeCityPercentage",
		65
	);
	
```

